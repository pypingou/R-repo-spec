%global packname  nice
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3
Release:          1%{?dist}
Summary:          Get or Set UNIX Niceness

Group:            Applications/Engineering 
License:          X11 (http://www.x.org/Downloads_terms.html)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
get or set UNIX priority (niceness) of running R process

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/nice/html
%doc %{rlibdir}/nice/DESCRIPTION
%{rlibdir}/nice/Meta
%{rlibdir}/nice/libs
%{rlibdir}/nice/NAMESPACE
%{rlibdir}/nice/R
%{rlibdir}/nice/help
%{rlibdir}/nice/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3-1
- initial package for Fedora