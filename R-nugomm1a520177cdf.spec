%global packname  nugomm1a520177cdf
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.4.1
Release:          1%{?dist}
Summary:          nugomm1a520177cdf

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/data/annotation/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-utils 

BuildRequires:    R-devel tex(latex) R-utils 

%description
A package containing an environment representing the NuGO_Mm1a520177.cdf

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
%doc %{rlibdir}/nugomm1a520177cdf/DESCRIPTION
%doc %{rlibdir}/nugomm1a520177cdf/html
%{rlibdir}/nugomm1a520177cdf/help
%{rlibdir}/nugomm1a520177cdf/data
%{rlibdir}/nugomm1a520177cdf/INDEX
%{rlibdir}/nugomm1a520177cdf/Meta
%{rlibdir}/nugomm1a520177cdf/NAMESPACE
%{rlibdir}/nugomm1a520177cdf/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.4.1-1
- initial package for Fedora