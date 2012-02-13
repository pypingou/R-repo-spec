%global packname  Formula
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{dist}
Summary:          Extended Model Formulas

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
Infrastructure for extended formulas with multiple parts on the right-hand
side and/or multiple responses on the left-hand side.

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
%doc %{rlibdir}/Formula/doc
%doc %{rlibdir}/Formula/html
%doc %{rlibdir}/Formula/DESCRIPTION
%doc %{rlibdir}/Formula/CITATION
%doc %{rlibdir}/Formula/NEWS
%{rlibdir}/Formula/R
%{rlibdir}/Formula/NAMESPACE
%{rlibdir}/Formula/help
%{rlibdir}/Formula/INDEX
%{rlibdir}/Formula/Meta

%changelog
* Mon Feb 13 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- Update to version 1.0.1

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora