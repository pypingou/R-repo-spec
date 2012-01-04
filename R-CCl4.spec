%global packname  CCl4
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.11
Release:          1%{?dist}
Summary:          Carbon Tetrachloride (CCl4) treated hepatocytes

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-limma 


BuildRequires:    R-devel tex(latex) R-Biobase R-limma



%description
NChannelSet for rat hepatocytes treated with Carbon Tetrachloride (CCl4)
data from LGC company.

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
%doc %{rlibdir}/CCl4/html
%doc %{rlibdir}/CCl4/doc
%doc %{rlibdir}/CCl4/DESCRIPTION
%{rlibdir}/CCl4/extdata
%{rlibdir}/CCl4/help
%{rlibdir}/CCl4/INDEX
%{rlibdir}/CCl4/data
%{rlibdir}/CCl4/Meta
%{rlibdir}/CCl4/NAMESPACE

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.11-1
- initial package for Fedora