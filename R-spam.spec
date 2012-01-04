%global packname  spam
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.27.0
Release:          1%{?dist}
Summary:          SPArse Matrix

Group:            Applications/Engineering 
License:          GPL | file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.27-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Set of function for sparse matrix algebra. Differences with SparseM/Matrix
are: (1) we only support (essentially) one sparse matrix format, (2) based
on transparent and simple structure(s), (3) tailored for MCMC calculations
within GMRF. (4) S3 and S4 like-"compatible" ...  and it is fast.

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
%doc %{rlibdir}/spam/NEWS
%doc %{rlibdir}/spam/html
%doc %{rlibdir}/spam/DESCRIPTION
%doc %{rlibdir}/spam/CITATION
%{rlibdir}/spam/Meta
%{rlibdir}/spam/data
%{rlibdir}/spam/help
%{rlibdir}/spam/0NEWS
%{rlibdir}/spam/INDEX
%{rlibdir}/spam/LICENSE
%{rlibdir}/spam/R
%{rlibdir}/spam/demo
%{rlibdir}/spam/libs
%{rlibdir}/spam/NAMESPACE
%{rlibdir}/spam/demodata

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.27.0-1
- initial package for Fedora