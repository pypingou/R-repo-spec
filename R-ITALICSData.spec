%global packname  ITALICSData
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.0.4
Release:          1%{?dist}
Summary:          ITALICSData

Group:            Applications/Engineering 
License:          GPL
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Data needed to use the ITALICS package

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
%doc %{rlibdir}/ITALICSData/html
%doc %{rlibdir}/ITALICSData/DESCRIPTION
%{rlibdir}/ITALICSData/data
%{rlibdir}/ITALICSData/NAMESPACE
%{rlibdir}/ITALICSData/Meta
%{rlibdir}/ITALICSData/help
%{rlibdir}/ITALICSData/extdata
%{rlibdir}/ITALICSData/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.4-1
- initial package for Fedora