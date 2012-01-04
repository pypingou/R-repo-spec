%global packname  gaschYHS
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.5
Release:          1%{?dist}
Summary:          ExpressionSet for response of yeast to heat shock and other environmental stresses

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Biobase 

BuildRequires:    R-devel tex(latex) R-Biobase 

%description
Data from PMID 11102521

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
%doc %{rlibdir}/gaschYHS/DESCRIPTION
%doc %{rlibdir}/gaschYHS/html
%{rlibdir}/gaschYHS/NAMESPACE
%{rlibdir}/gaschYHS/help
%{rlibdir}/gaschYHS/data
%{rlibdir}/gaschYHS/Meta
%{rlibdir}/gaschYHS/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.5-1
- initial package for Fedora