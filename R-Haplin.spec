%global packname  Haplin
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          3.5
Release:          1%{?dist}
Summary:          Analyzing case-parent triad and/or case-control data with SNP haplotypes

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-mgcv 

BuildRequires:    R-devel tex(latex) R-MASS R-mgcv 

%description
Haplin performs a genetic association analysis of case-parent triad (trio)
data with multiple markers. It can also incorporate complete or incomplete
control triads, for instance independent control children. Estimation is
based on haplotypes, for instance SNP haplotypes, even though phase is not
known from the genetic data. Haplin estimates relative risk (RR +
conf.int.) and p-value associated with each haplotype. It uses maximum
likelihood estimation to make optimal use of data from triads with missing
genotypic data, for instance if some SNPs has not been typed for some
individuals. Haplin also allows estimation of effects of maternal
haplotypes, particularly appropriate in perinatal epidemiology.

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
%doc %{rlibdir}/Haplin/DESCRIPTION
%doc %{rlibdir}/Haplin/html
%{rlibdir}/Haplin/R
%{rlibdir}/Haplin/Meta
%{rlibdir}/Haplin/help
%{rlibdir}/Haplin/INDEX
%{rlibdir}/Haplin/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.5-1
- initial package for Fedora