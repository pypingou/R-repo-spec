%global packname  sra
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Selection Response Analysis

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats4 

BuildRequires:    R-devel tex(latex) R-stats4 

%description
This package (sra) provides a set of tools to analyse artificial-selection
response datasets. The data typically feature for several generations the
average value of a trait in a population, the variance of the trait, the
population size and the average value of the parents that were chosen to
breed. Sra implements two families of models aiming at describing the
dynamics of the genetic architecture of the trait during the selection
response. The first family relies on purely descriptive (phenomenological)
models, based on an autoregressive framework. The second family provides
different mechanistic models, accounting e.g. for inbreeding, mutations,
genetic and environmental canalization, or epistasis. The parameters
underlying the dynamics of the time series are estimated by maximum
likelihood. The sra package thus provides (i) a wrapper for the R
functions mle() and optim() aiming at fitting in a convenient way a
predetermined set of models, and (ii) some functions to plot and analyze
the output of the models.

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
%doc %{rlibdir}/sra/DESCRIPTION
%doc %{rlibdir}/sra/html
%{rlibdir}/sra/NAMESPACE
%{rlibdir}/sra/Meta
%{rlibdir}/sra/help
%{rlibdir}/sra/INDEX
%{rlibdir}/sra/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora