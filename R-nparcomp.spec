%global packname  nparcomp
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          nparcomp-package

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-multcomp R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-multcomp R-mvtnorm 

%description
With this package, it is possible to compute nonparametric simultaneous
confidence intervals for relative contrast effects in the unbalanced one
way layout. Moreover, it computes simultaneous p-values. The simultaneous
confidence intervals can be computed using multivariate normal
distribution, multivariate t-distribution with a Satterthwaite
Approximation of the degree of freedom or using multivariate range
preserving transformations with Logit or Probit as transformation
function. 2 sample comparisons can be performed with the same methods
described above. There is no assumption on the underlying distribution
function, only that the data have to be at least ordinal numbers.

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
%doc %{rlibdir}/nparcomp/DESCRIPTION
%doc %{rlibdir}/nparcomp/html
%{rlibdir}/nparcomp/R
%{rlibdir}/nparcomp/INDEX
%{rlibdir}/nparcomp/help
%{rlibdir}/nparcomp/data
%{rlibdir}/nparcomp/Meta

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora