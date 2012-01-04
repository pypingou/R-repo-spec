%global packname  pomp
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.39.4
Release:          1%{?dist}
Summary:          Statistical inference for partially observed Markov processes

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.39-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-methods R-graphics R-mvtnorm R-subplex R-deSolve 

BuildRequires:    R-devel tex(latex) R-stats R-methods R-graphics R-mvtnorm R-subplex R-deSolve 

%description
Inference methods for partially-observed Markov processes

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
%doc %{rlibdir}/pomp/NEWS
%doc %{rlibdir}/pomp/html
%doc %{rlibdir}/pomp/DESCRIPTION
%doc %{rlibdir}/pomp/doc
%doc %{rlibdir}/pomp/CITATION
%{rlibdir}/pomp/NAMESPACE
%{rlibdir}/pomp/include
%{rlibdir}/pomp/TODO
%{rlibdir}/pomp/data-R
%{rlibdir}/pomp/CHANGES_0.29-1.txt
%{rlibdir}/pomp/ChangeLog
%{rlibdir}/pomp/examples
%{rlibdir}/pomp/R
%{rlibdir}/pomp/help
%{rlibdir}/pomp/libs
%{rlibdir}/pomp/O_CHANGES
%{rlibdir}/pomp/LICENSE
%{rlibdir}/pomp/INDEX
%{rlibdir}/pomp/Meta
%{rlibdir}/pomp/data
%{rlibdir}/pomp/GPL

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.39.4-1
- initial package for Fedora