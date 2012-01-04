%global packname  ump
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.2
Release:          1%{?dist}
Summary:          Uniformly Most Powerful Tests

Group:            Applications/Engineering 
License:          X11 (http://www.x.org/Downloads_terms.html)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
see title

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
%doc %{rlibdir}/ump/doc
%doc %{rlibdir}/ump/html
%doc %{rlibdir}/ump/DESCRIPTION
%{rlibdir}/ump/NAMESPACE
%{rlibdir}/ump/INDEX
%{rlibdir}/ump/Meta
%{rlibdir}/ump/help
%{rlibdir}/ump/R
%{rlibdir}/ump/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.2-1
- initial package for Fedora