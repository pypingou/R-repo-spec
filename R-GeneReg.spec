%global packname  GeneReg
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.2
Release:          1%{?dist}
Summary:          Construct time delay gene regulatory network

Group:            Applications/Engineering 
License:          LGPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-splines R-igraph 

BuildRequires:    R-devel tex(latex) R-splines R-igraph 

%description
GeneReg is an R package for inferring time delay gene regulatory network
using time course gene expression profiles. The main idea of time delay
linear model is to fit a linear regression model using a set of putative
regulators to estimate the transcription pattern of a specific target

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
%doc %{rlibdir}/GeneReg/DESCRIPTION
%doc %{rlibdir}/GeneReg/html
%{rlibdir}/GeneReg/R
%{rlibdir}/GeneReg/INDEX
%{rlibdir}/GeneReg/help
%{rlibdir}/GeneReg/data
%{rlibdir}/GeneReg/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.2-1
- initial package for Fedora