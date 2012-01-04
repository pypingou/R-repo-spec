%global packname  Benchmarking
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.20
Release:          1%{?dist}
Summary:          Benchmark and frontier analysis using DEA and SFA

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lpSolveAPI R-ucminf 

BuildRequires:    R-devel tex(latex) R-lpSolveAPI R-ucminf 

%description
The package contains methods to support frontier analysis. It covers Data
Envelopment Analysis (DEA). DEA is supported under different technology
assumptions (fdh, vrs, drs, crs, irs, add/frh, and fdh+), and using
different efficiency measures (input based, output based, hyperbolic
graph, additive, super, and directional efficency). Peers and slacks are
available, partial price information can be included, and optimal cost,
revenue and profit can be calculated. Evaluation of mergers is also
supported.  Methods for graphing the technology sets are also included.
The package also support comparative methods based on Stochastic Frontier
Analyses (SFA). In general, the methods can be used to solve not only
standard models, but also many other model variants. The package
complements the book, Bogetoft and Otto, Benchmarking with DEA, SFA, and
R, Springer-Verlag, 2011, but can of course also be used as a stand-alone

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
%doc %{rlibdir}/Benchmarking/DESCRIPTION
%doc %{rlibdir}/Benchmarking/CITATION
%doc %{rlibdir}/Benchmarking/NEWS
%doc %{rlibdir}/Benchmarking/html
%{rlibdir}/Benchmarking/R
%{rlibdir}/Benchmarking/NAMESPACE
%{rlibdir}/Benchmarking/Meta
%{rlibdir}/Benchmarking/data
%{rlibdir}/Benchmarking/help
%{rlibdir}/Benchmarking/INDEX

%changelog
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.20-1
- initial package for Fedora