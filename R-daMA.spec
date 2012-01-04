%global packname  daMA
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.26.0
Release:          1%{?dist}
Summary:          Efficient design and analysis of factorial two-colour microarray data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package contains functions for the efficient design of factorial
two-colour microarray experiments and for the statistical analysis of
factorial microarray data. Statistical details are described in Bretz et
al. (2003, submitted)

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
%doc %{rlibdir}/daMA/DESCRIPTION
%doc %{rlibdir}/daMA/html
%{rlibdir}/daMA/data
%{rlibdir}/daMA/Meta
%{rlibdir}/daMA/R
%{rlibdir}/daMA/help
%{rlibdir}/daMA/INDEX
%{rlibdir}/daMA/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.26.0-1
- initial package for Fedora