%global packname  FisherEM
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.2
Release:          1%{?dist}
Summary:          Model-Based Clustering in the Fisher Discriminative Subspace

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-e1071 

BuildRequires:    R-devel tex(latex) R-MASS R-e1071 

%description
Model-Based Clustering in the Fisher Discriminative Subspace provides a
low-dimensional discriminative representation of the clustered data. To
find a parsimonious and discriminative fit for the data this method uses
discriminative latent model (DLM). The Fisher EM algorithm estimates the
parameters of DLM models in order to cluster and visualize the clustered

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
%doc %{rlibdir}/FisherEM/html
%doc %{rlibdir}/FisherEM/DESCRIPTION
%{rlibdir}/FisherEM/R
%{rlibdir}/FisherEM/Meta
%{rlibdir}/FisherEM/demo
%{rlibdir}/FisherEM/NAMESPACE
%{rlibdir}/FisherEM/help
%{rlibdir}/FisherEM/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.2-1
- initial package for Fedora