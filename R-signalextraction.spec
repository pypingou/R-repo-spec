%global packname  signalextraction
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0.3
Release:          1%{?dist}
Summary:          Real-Time Signal Extraction (Direct Filter Approach)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The Direct Filter Approach (DFA) provides efficient estimates of signals
at the current boundary of time series in real-time. For that purpose,
one-sided ARMA-filters are computed by minimizing customized error
criteria. The DFA can be used for estimating either the level or
turning-points of a series, knowing that both criteria are incongruent. In
the context of real-time turning- point detection, various risk-profiles
can be operationalized, which account for the speed and/or the reliability
of the one- sided filter.

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
%doc %{rlibdir}/signalextraction/html
%doc %{rlibdir}/signalextraction/doc
%doc %{rlibdir}/signalextraction/DESCRIPTION
%{rlibdir}/signalextraction/data
%{rlibdir}/signalextraction/R
%{rlibdir}/signalextraction/NAMESPACE
%{rlibdir}/signalextraction/help
%{rlibdir}/signalextraction/Meta
%{rlibdir}/signalextraction/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.3-1
- initial package for Fedora