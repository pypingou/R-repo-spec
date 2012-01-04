%global packname  RODM
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          R interface to Oracle Data Mining

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-RODBC 

BuildRequires:    R-devel tex(latex) R-RODBC 

%description
This package implements an interface to Oracle Data Mining (ODM). It
provides an ideal environment for rapid development of demos and proof of
concept data mining studies. It facilitates the prototyping of vertical
applications and makes ODM and the RDBMS environment easily accessible to
statisticians and data analysts familiar with R but not fluent in SQL or
familiar with the database environment. It also facilitates the
benchmarking and testing of ODM functionality including the production of
summary statistics, performance metrics and graphics. It enables the
scripting and control of production data mining methodologies from a
high-level environment. Oracle Data Mining (ODM) is an option of Oracle
Relational Database Management System (RDBMS) Enterprise Edition (EE). It
contains several data mining and data analysis algorithms for
classification, prediction, regression, clustering, associations, feature
selection, anomaly detection, feature extraction, and specialized
analytics. It provides means for the creation, management and operational
deployment of data mining models inside the database environment. For more
information consult the entry for "Oracle Data Mining" in Wikipedia

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
%doc %{rlibdir}/RODM/html
%doc %{rlibdir}/RODM/DESCRIPTION
%{rlibdir}/RODM/INDEX
%{rlibdir}/RODM/help
%{rlibdir}/RODM/Meta
%{rlibdir}/RODM/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora