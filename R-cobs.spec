%global packname  cobs
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.2
Release:          1%{?dist}
Summary:          COBS -- Constrained B-splines (Sparse matrix based)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-SparseM R-quantreg R-splines R-grDevices R-graphics R-stats R-utils 


BuildRequires:    R-devel tex(latex) R-SparseM R-quantreg R-splines R-grDevices R-graphics R-stats R-utils



%description
Qualitatively Constrained (Regression) Smoothing via Linear Programming
and Sparse Matrices.

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
%doc %{rlibdir}/cobs/html
%doc %{rlibdir}/cobs/DESCRIPTION
%{rlibdir}/cobs/Meta
%{rlibdir}/cobs/data
%{rlibdir}/cobs/help
%{rlibdir}/cobs/INDEX
%{rlibdir}/cobs/util.R
%{rlibdir}/cobs/R
%{rlibdir}/cobs/libs
%{rlibdir}/cobs/NAMESPACE
%{rlibdir}/cobs/scripts

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.2-1
- initial package for Fedora