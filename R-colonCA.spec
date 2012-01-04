%global packname  colonCA
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.4.8
Release:          1%{?dist}
Summary:          exprSet for Alon et al. (1999) colon cancer data

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Biobase 

BuildRequires:    R-devel tex(latex) R-Biobase 

%description
exprSet for Alon et al. (1999) colon cancer data

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
%doc %{rlibdir}/colonCA/DESCRIPTION
%doc %{rlibdir}/colonCA/html
%{rlibdir}/colonCA/INDEX
%{rlibdir}/colonCA/help
%{rlibdir}/colonCA/data
%{rlibdir}/colonCA/Meta
%{rlibdir}/colonCA/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.8-1
- initial package for Fedora