%global packname  wq
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.4
Release:          1%{?dist}
Summary:          Exploring water quality monitoring data

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-zoo 

BuildRequires:    R-devel tex(latex) R-methods R-zoo 

%description
Functions to assist in the processing and exploration of data from
monitoring programs for aquatic ecosystems. The name "wq" stands for
"water quality" and reflects a focus on time series data for physical and
chemical properties of water, as well as the plankton. The package is
intended for programs that sample approximately monthly at discrete
stations, a feature of many legacy data sets. Although our emphasis is on
aquatic ecosystems, most of the functions should be useful for analysis of
similar-frequency time series regardless of the subject matter.

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
%doc %{rlibdir}/wq/doc
%doc %{rlibdir}/wq/DESCRIPTION
%doc %{rlibdir}/wq/html
%doc %{rlibdir}/wq/CITATION
%{rlibdir}/wq/R
%{rlibdir}/wq/help
%{rlibdir}/wq/Meta
%{rlibdir}/wq/data
%{rlibdir}/wq/NAMESPACE
%{rlibdir}/wq/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.4-1
- initial package for Fedora