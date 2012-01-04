%global packname  irtoys
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          Simple interface to the estimation and plotting of IRT models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-sm R-ltm 

BuildRequires:    R-devel tex(latex) R-sm R-ltm 

%description
Provides a simple common interface to the estimation of item parameters in
IRT models for binary responses with three different programs (ICL,
BILOG-MG, and ltm, and a variety of functions useful with IRT models.

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
%doc %{rlibdir}/irtoys/DESCRIPTION
%doc %{rlibdir}/irtoys/html
%{rlibdir}/irtoys/Meta
%{rlibdir}/irtoys/data
%{rlibdir}/irtoys/NAMESPACE
%{rlibdir}/irtoys/R
%{rlibdir}/irtoys/INDEX
%{rlibdir}/irtoys/help

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.4-1
- initial package for Fedora