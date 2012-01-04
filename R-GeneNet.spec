%global packname  GeneNet
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.4
Release:          1%{?dist}
Summary:          Modeling and Inferring Gene Networks

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-corpcor R-longitudinal R-fdrtool 

BuildRequires:    R-devel tex(latex) R-corpcor R-longitudinal R-fdrtool 

%description
GeneNet is a package for analyzing gene expression (time series) data with
focus on the inference of gene networks. In particular, GeneNet implements
the methods of Schaefer and Strimmer (2005a,b,c) and Opgen-Rhein and
Strimmer (2006, 2007) for learning large-scale gene association networks
(including assignment of putative directions).

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
%doc %{rlibdir}/GeneNet/DESCRIPTION
%doc %{rlibdir}/GeneNet/doc
%doc %{rlibdir}/GeneNet/html
%doc %{rlibdir}/GeneNet/NEWS
%{rlibdir}/GeneNet/Meta
%{rlibdir}/GeneNet/INDEX
%{rlibdir}/GeneNet/R
%{rlibdir}/GeneNet/LICENSE
%{rlibdir}/GeneNet/help
%{rlibdir}/GeneNet/data

%changelog
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.4-1
- initial package for Fedora