%global packname  ICEinfer
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Incremental Cost-Effectiveness (ICE) Statistical Inference from Two Unbiased Samples

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lattice 

BuildRequires:    R-devel tex(latex) R-lattice 

%description
Given two unbiased samples of patient level data on cost and effectiveness
for a pair of treatments, make head-to-head treatment comparisons by (i)
generating the bivariate bootstrap resampling distribution of ICE
uncertainty for a specified value of the shadow price of health, lambda,
(ii) form the wedge-shaped ICE confidence region with specified confidence
fraction within [0.50, 0.99] that is equivariant with respect to changes
in lambda, (iii) color the bootstrap outcomes within the above confidence
wedge with economic preferences from an ICE map with specified values of
lambda, beta and gamma parameters, (iv) display VAGR and ALICE
acceptability curves, and (v) display indifference (iso-preference) curves
from an ICE map with specified values of lambda, beta and gamma or eta

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
%doc %{rlibdir}/ICEinfer/html
%doc %{rlibdir}/ICEinfer/DESCRIPTION
%{rlibdir}/ICEinfer/ICEinR.pdf
%{rlibdir}/ICEinfer/INDEX
%{rlibdir}/ICEinfer/Meta
%{rlibdir}/ICEinfer/data
%{rlibdir}/ICEinfer/help
%{rlibdir}/ICEinfer/R
%{rlibdir}/ICEinfer/NAMESPACE
%{rlibdir}/ICEinfer/demo

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.0-1
- initial package for Fedora