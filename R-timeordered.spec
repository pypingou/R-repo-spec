%global packname  timeordered
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9
Release:          1%{?dist}
Summary:          Time-ordered and time-aggregated network analyses

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-igraph R-plyr 


BuildRequires:    R-devel tex(latex) R-igraph R-plyr



%description
Methods for incorporating time into network analysis. Construction of
time-ordered networks (temporal graphs). Shortest-time and
shortest-path-length analyses. Resource spread calculations. Data
resampling and rarefaction for null model construction. Reduction to
time-aggregated networks with variable window sizes; application of common
descriptive statistics to these networks. Vector clock latencies. Plotting
functionalities & full compatibility with all network methods in the
igraph library.

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
%changelog
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9-1
- initial package for Fedora