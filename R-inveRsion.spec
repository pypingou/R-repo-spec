%global packname  inveRsion
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Inversions in genotype data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-haplo.stats 

BuildRequires:    R-devel tex(latex) R-methods R-haplo.stats 

%description
Package to find genetic inversions in genotype (SNP array) data.

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
%doc %{rlibdir}/inveRsion/doc
%doc %{rlibdir}/inveRsion/DESCRIPTION
%doc %{rlibdir}/inveRsion/html
%{rlibdir}/inveRsion/INDEX
%{rlibdir}/inveRsion/NAMESPACE
%{rlibdir}/inveRsion/help
%{rlibdir}/inveRsion/data
%{rlibdir}/inveRsion/extdata
%{rlibdir}/inveRsion/R
%{rlibdir}/inveRsion/libs
%{rlibdir}/inveRsion/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.0-1
- initial package for Fedora