%global packname  CircStats
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.4
Release:          1%{?dist}
Summary:          Circular Statistics, from "Topics in circular Statistics" (2001)

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-boot 

BuildRequires:    R-devel tex(latex) R-MASS R-boot 

%description
Circular Statistics, from "Topics in circular Statistics" (2001) S. Rao
Jammalamadaka and A. SenGupta, World Scientific.

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
%doc %{rlibdir}/CircStats/html
%doc %{rlibdir}/CircStats/DESCRIPTION
%{rlibdir}/CircStats/NAMESPACE
%{rlibdir}/CircStats/INDEX
%{rlibdir}/CircStats/Meta
%{rlibdir}/CircStats/data
%{rlibdir}/CircStats/R
%{rlibdir}/CircStats/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.4-1
- initial package for Fedora