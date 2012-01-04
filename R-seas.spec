%global packname  seas
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.9
Release:          1%{?dist}
Summary:          Seasonal analysis and graphics, especially for climatology

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-9.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Capable of deriving seasonal statistics, such as "normals", and analysis
of seasonal data, such as departures. This package also has graphics
capabilities for representing seasonal data, including boxplots for
seasonal parameters, and bars for summed normals. There are many specific
functions related to climatology, including precipitation normals,
temperature normals, cumulative precipitation departures and precipitation
interarrivals. However, this package is designed to represent any
time-varying parameter with a discernible seasonal signal, such as found
in hydrology and ecology.

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
%doc %{rlibdir}/seas/CITATION
%doc %{rlibdir}/seas/DESCRIPTION
%doc %{rlibdir}/seas/html
%{rlibdir}/seas/R
%{rlibdir}/seas/help
%{rlibdir}/seas/INDEX
%{rlibdir}/seas/data
%{rlibdir}/seas/Meta
%{rlibdir}/seas/NAMESPACE
%{rlibdir}/seas/ChangeLog
%{rlibdir}/seas/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.9-1
- initial package for Fedora