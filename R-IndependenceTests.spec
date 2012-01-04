%global packname  IndependenceTests
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Nonparametric tests of independence between random vectors.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-xtable 

BuildRequires:    R-devel tex(latex) R-xtable 

%description
Functions for testing mutual independence between many numerical random
vectors or serial independence of a multivariate stationary sequence. The
proposed test works when some or all of the marginal distributions are
singular with respect to Lebesgue measure.

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
%doc %{rlibdir}/IndependenceTests/DESCRIPTION
%doc %{rlibdir}/IndependenceTests/CITATION
%doc %{rlibdir}/IndependenceTests/html
%{rlibdir}/IndependenceTests/R
%{rlibdir}/IndependenceTests/NAMESPACE
%{rlibdir}/IndependenceTests/data
%{rlibdir}/IndependenceTests/INDEX
%{rlibdir}/IndependenceTests/libs
RPM build errors:
%{rlibdir}/IndependenceTests/help
%{rlibdir}/IndependenceTests/HISTORY
%{rlibdir}/IndependenceTests/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora