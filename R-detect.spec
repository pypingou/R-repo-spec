%global packname  detect
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Analyzing Wildlife Data with Detection Error

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The package implements models to analyze site occupancy and count data
models with detection error.  Development was funded by the Alberta
Biodiversity Monitoring Institute.

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
%doc %{rlibdir}/detect/DESCRIPTION
%doc %{rlibdir}/detect/COPYING
%doc %{rlibdir}/detect/html
%{rlibdir}/detect/R
%{rlibdir}/detect/Meta
%{rlibdir}/detect/data
%{rlibdir}/detect/INDEX
%{rlibdir}/detect/ChangeLog
%{rlibdir}/detect/help
%{rlibdir}/detect/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.0-1
- initial package for Fedora