%global packname  pmml
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.27
Release:          1%{?dist}
Summary:          Generate PMML for various models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-XML 

BuildRequires:    R-devel tex(latex) R-XML 

%description
The Predictive Modelling Markup Language (PMML) is a language for
representing models, in an application independent way. Such models can
then be loaded into other applications supporting PMML, including ADAPA
from Zementis, Teradata Warehouse Miner and IBM's DB2. The package
provides a generic pmml function to generate pmml for an object. Using a
S3 generic function the approriate method for the class of the supplied
object is dispatched. The package currently supports the export of PMML
for linear regression, SVMs, rpart classification trees,
randomSurvivalForest forest models, and kmeans clusters. This package is
part of the Rattle toolkit.

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
%doc %{rlibdir}/pmml/DESCRIPTION
%doc %{rlibdir}/pmml/html
%{rlibdir}/pmml/R
%{rlibdir}/pmml/NAMESPACE
%{rlibdir}/pmml/help
%{rlibdir}/pmml/INDEX
%{rlibdir}/pmml/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.27-1
- initial package for Fedora