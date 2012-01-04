%global packname  LiquidAssociation
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.8.0
Release:          1%{?dist}
Summary:          LiquidAssociation

Group:            Applications/Engineering 
License:          GPL (>=3)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-geepack R-methods R-yeastCC R-org.Sc.sgd.db 
Requires:         R-Biobase R-graphics R-grDevices R-methods R-stats 

BuildRequires:    R-devel tex(latex) R-geepack R-methods R-yeastCC R-org.Sc.sgd.db
BuildRequires:    R-Biobase R-graphics R-grDevices R-methods R-stats 


%description
The package contains functions for calculate direct and model-based
estimators for liquid association. It also provides functions for testing
the existence of liquid association given a gene triplet data.

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
%changelog
* Mon Dec 12 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.8.0-1
- initial package for Fedora