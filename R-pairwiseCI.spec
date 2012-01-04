%global packname  pairwiseCI
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.19
Release:          1%{?dist}
Summary:          Confidence intervals for two sample comparisons

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-19.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats R-exactRankTests R-boot R-mratios R-binMto R-MASS R-MCPAN 


BuildRequires:    R-devel tex(latex) R-stats R-exactRankTests R-boot R-mratios R-binMto R-MASS R-MCPAN



%description
Calculation of the parametric, nonparametric confidence intervals for the
difference or ratio of location parameters and for the difference, ratio
and odds-ratio of binomial proportions for comparison of independent
samples. CI are not adjusted for multiplicity. A by statement allows
calculation of CI separately for the levels of further factors. Please
note that, when a (generalized) linear model can be reasonably assumed,
there are smarter methods for CI calculation available than are
implemented in this package!

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
%changelog
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.19-1
- initial package for Fedora