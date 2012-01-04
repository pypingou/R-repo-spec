%global packname  nonrandom
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Stratification and matching by the propensity score

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lme4 


BuildRequires:    R-devel tex(latex) R-lme4



%description
This package offers a comprehensive data analysis if stratification and
matching by the propensity score is done. Several functions are
implemented, starting from the selection of the propensity score model up
to estimating propensity score based treatment or exposure effects. All
functions can be applied separately as well as combined.

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
%doc %{rlibdir}/nonrandom/doc
%doc %{rlibdir}/nonrandom/html
%doc %{rlibdir}/nonrandom/DESCRIPTION
%{rlibdir}/nonrandom/data
%{rlibdir}/nonrandom/R
%{rlibdir}/nonrandom/INDEX
%{rlibdir}/nonrandom/help
%{rlibdir}/nonrandom/NAMESPACE
%{rlibdir}/nonrandom/Meta

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora