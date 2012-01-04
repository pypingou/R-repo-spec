%global packname  coin
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.20
Release:          1%{?dist}
Summary:          Conditional Inference Procedures in a Permutation Test Framework

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-20.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-survival R-mvtnorm R-modeltools 


BuildRequires:    R-devel tex(latex) R-methods R-survival R-mvtnorm R-modeltools



%description
Conditional inference procedures for the general independence problem
including two-sample, K-sample (non-parametric ANOVA), correlation,
censored, ordered and multivariate problems.

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
%doc %{rlibdir}/coin/doc
%doc %{rlibdir}/coin/CITATION
%doc %{rlibdir}/coin/DESCRIPTION
%doc %{rlibdir}/coin/NEWS
%doc %{rlibdir}/coin/html
%{rlibdir}/coin/libs
%{rlibdir}/coin/data
%{rlibdir}/coin/README
%{rlibdir}/coin/Meta
%{rlibdir}/coin/R
%{rlibdir}/coin/help
%{rlibdir}/coin/INDEX
%{rlibdir}/coin/documentation
%{rlibdir}/coin/NAMESPACE

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.20-1
- initial package for Fedora