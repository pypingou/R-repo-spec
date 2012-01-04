%global packname  predictionet
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Inference for predictive networks designed for (but not limited to) genomic data

Group:            Applications/Engineering 
License:          Artistic 2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-igraph R-catnet 
Requires:         R-penalized 

BuildRequires:    R-devel tex(latex) R-igraph R-catnet
BuildRequires:    R-penalized 


%description
This package contains a set of functions related to network inference
combining genomic data and prior information extracted from biomedical
literature and structured biological databases. The main function is able
to generate networks using Bayesian or regression-based inference methods;
while the former is limited to < 100 of variables, the latter may infer
networks with hundreds of variables. Several statistics at the edge and
node levels have been implemented (edge stability, predictive ability of
each node, ...) in order to help the user to focus on high quality
subnetworks. Ultimately, this package is used in the 'Predictive Networks'
web application developed by the Dana-Farber Cancer Institute in
collaboration with Entagen.

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
%doc %{rlibdir}/predictionet/doc
%doc %{rlibdir}/predictionet/DESCRIPTION
%doc %{rlibdir}/predictionet/html
%{rlibdir}/predictionet/R
%{rlibdir}/predictionet/extdata
%{rlibdir}/predictionet/INDEX
%{rlibdir}/predictionet/data
%{rlibdir}/predictionet/Meta
%{rlibdir}/predictionet/NAMESPACE
%{rlibdir}/predictionet/help
%{rlibdir}/predictionet/libs

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora