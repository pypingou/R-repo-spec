%global packname  HTSCluster
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Clustering high throughput sequencing (HTS) data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package implements two parameterizations of a Poisson mixture model
to cluster observations (e.g., genes) in high throughput sequencing data.
Parameter estimation is performed using either the EM or CEM algorithm,
and the BIC or ICL criteria are used for model selection (i.e., to choose
the number of clusters).

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
%doc %{rlibdir}/HTSCluster/html
%doc %{rlibdir}/HTSCluster/DESCRIPTION
%{rlibdir}/HTSCluster/NAMESPACE
%{rlibdir}/HTSCluster/help
%{rlibdir}/HTSCluster/Meta
%{rlibdir}/HTSCluster/R
%{rlibdir}/HTSCluster/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora