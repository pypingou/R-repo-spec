%global packname  mvngGrAd
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Software for moving grid adjustment in plant breeding field trials

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-stats 

BuildRequires:    R-devel tex(latex) R-methods R-stats 

%description
Package for moving grid adjustment in plant breeding field trials.

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
%doc %{rlibdir}/mvngGrAd/doc
%doc %{rlibdir}/mvngGrAd/CITATION
%doc %{rlibdir}/mvngGrAd/DESCRIPTION
%doc %{rlibdir}/mvngGrAd/html
%{rlibdir}/mvngGrAd/INDEX
%{rlibdir}/mvngGrAd/R
%{rlibdir}/mvngGrAd/NAMESPACE
%{rlibdir}/mvngGrAd/Meta
%{rlibdir}/mvngGrAd/help
RPM build errors:

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.2-1
- initial package for Fedora