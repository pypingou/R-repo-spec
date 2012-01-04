%global packname  logspline
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.1.3
Release:          1%{?dist}
Summary:          Logspline density estimation routines

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Routines for the logspline density estimation. oldlogspline uses the same
algorithm as the logspline 1.0.x package - the Kooperberg and Stone (1992)
algorithm (with an improved interface). The recomended routine logspline
uses an algorithm from Stone et al (1997).

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
%doc %{rlibdir}/logspline/DESCRIPTION
%doc %{rlibdir}/logspline/html
%{rlibdir}/logspline/R
%{rlibdir}/logspline/help
%{rlibdir}/logspline/NAMESPACE
%{rlibdir}/logspline/INDEX
%{rlibdir}/logspline/Meta
%{rlibdir}/logspline/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1.3-1
- initial package for Fedora