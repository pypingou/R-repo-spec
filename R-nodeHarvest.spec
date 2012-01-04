%global packname  nodeHarvest
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.5
Release:          1%{?dist}
Summary:          Node Harvest for regression and classification

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-quadprog R-randomForest 

BuildRequires:    R-devel tex(latex) R-quadprog R-randomForest 

%description
Node harvest is a simple interpretable tree-like estimator for
high-dimensional regression and classification. A few nodes are selected
from an initially large ensemble of nodes, each associated with a positive
weight. New observations can fall into one or several nodes and
predictions are the weighted average response across all these groups. The
package offers visualization of the estimator. Predictions can return the
nodes a new observation fell into, along with the mean response of
training observations in each node, offering a simple explanation of the

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
%doc %{rlibdir}/nodeHarvest/DESCRIPTION
%doc %{rlibdir}/nodeHarvest/html
%{rlibdir}/nodeHarvest/INDEX
%{rlibdir}/nodeHarvest/help
%{rlibdir}/nodeHarvest/R
%{rlibdir}/nodeHarvest/Meta
%{rlibdir}/nodeHarvest/NAMESPACE
%{rlibdir}/nodeHarvest/data

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5-1
- initial package for Fedora