%global packname  hints
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.1.1
Release:          1%{?dist}
Summary:          Provide hints on what to do next

Group:            Applications/Engineering 
License:          GPL version 2 or newer
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Gives hints on what functions you might want to apply to an object you
have created.

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
%doc %{rlibdir}/hints/doc
%doc %{rlibdir}/hints/html
%doc %{rlibdir}/hints/DESCRIPTION
%{rlibdir}/hints/NAMESPACE
%{rlibdir}/hints/INDEX
%{rlibdir}/hints/R
%{rlibdir}/hints/help
%{rlibdir}/hints/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1.1-1
- initial package for Fedora