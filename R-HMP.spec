%global packname  HMP
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Hypothesis Testing and Power Calculations for Comparing Metagenomic Samples from HMP

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lattice R-MCMCpack R-maxLik R-binomSamSize R-Hmisc R-zipfR R-vegan R-dirmult 


BuildRequires:    R-devel tex(latex) R-lattice R-MCMCpack R-maxLik R-binomSamSize R-Hmisc R-zipfR R-vegan R-dirmult



%description
This package provides several functions to perform formal hypothesis
testing, and power and sample size calculations for human microbiome
experiments. Dirichlet-Multinomial distribution is proposed for modeling
the species abundance distributions of human microbiota (ranked bacterial
taxa counts).

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora