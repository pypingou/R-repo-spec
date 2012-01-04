%global packname  StreamMetabolism
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.03.3
Release:          1%{?dist}
Summary:          Stream Metabolism-A package for calculating single station metabolism from diurnal Oxygen curves

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.03-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-zoo R-chron R-maptools 

BuildRequires:    R-devel tex(latex) R-zoo R-chron R-maptools 

%description
This package contains functions for calculating GPP, NDM, and R from
single station diurnal Oxygen curves

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
%doc %{rlibdir}/StreamMetabolism/DESCRIPTION
%doc %{rlibdir}/StreamMetabolism/CITATION
%doc %{rlibdir}/StreamMetabolism/html
%{rlibdir}/StreamMetabolism/R
%{rlibdir}/StreamMetabolism/data
%{rlibdir}/StreamMetabolism/help
%{rlibdir}/StreamMetabolism/INDEX
%{rlibdir}/StreamMetabolism/Meta

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.03.3-1
- initial package for Fedora