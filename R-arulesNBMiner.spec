%global packname  arulesNBMiner
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Mining NB-Frequent Itemsets and NB-Precise Rules

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-arules R-rJava 

BuildRequires:    R-devel tex(latex) R-arules R-rJava 

%description
NBMiner is an implementation of the model-based mining algorithm for
mining NB-frequent itemsets presented in "Michael Hahsler. A model-based
frequency constraint for mining associations from transaction data. Data
Mining and Knowledge Discovery, 13(2):137-166, September 2006." In
addition an extension for NB-precise rules is implemented.

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
%doc %{rlibdir}/arulesNBMiner/html
%doc %{rlibdir}/arulesNBMiner/DESCRIPTION
%{rlibdir}/arulesNBMiner/R
%{rlibdir}/arulesNBMiner/java
%{rlibdir}/arulesNBMiner/NAMESPACE
%{rlibdir}/arulesNBMiner/Meta
%{rlibdir}/arulesNBMiner/help
%{rlibdir}/arulesNBMiner/data
%{rlibdir}/arulesNBMiner/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora