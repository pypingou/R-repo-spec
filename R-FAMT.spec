%global packname  FAMT
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.3
Release:          1%{?dist}
Summary:          Factor Analysis for Multiple Testing (FAMT) : simultaneous tests under dependence in high-dimensional data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-mnormt R-impute 

BuildRequires:    R-devel tex(latex) R-mnormt R-impute 

%description
The method proposed in this package takes into account the impact of
dependence on the multiple testing procedures for high-throughput data as
proposed by Friguet et al. (2009). The common information shared by all
the variables is modeled by a factor analysis structure. The number of
factors considered in the model is chosen to reduce the false discoveries
variance in multiple tests. The model parameters are estimated thanks to
an EM algorithm. Adjusted tests statistics are derived, as well as the
associated p-values. The proportion of true null hypotheses (an important
parameter when controlling the false discovery rate) is also estimated
from the FAMT model. Graphics are proposed to interpret and describe the

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
%doc %{rlibdir}/FAMT/CITATION
%doc %{rlibdir}/FAMT/DESCRIPTION
%doc %{rlibdir}/FAMT/html
%{rlibdir}/FAMT/INDEX
%{rlibdir}/FAMT/help
%{rlibdir}/FAMT/data
%{rlibdir}/FAMT/Meta
%{rlibdir}/FAMT/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.3-1
- initial package for Fedora