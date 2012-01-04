%global packname  SQUAREM
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2010.12.1
Release:          1%{?dist}
Summary:          Squared extrapolation methods for accelerating fixed-point iterations

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2010.12-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Algorithms for accelerating the convergence of slow, monotone sequences
from smooth, contraction mapping such as the EM algorithm. It can be used
to accelerate any smooth, linearly convergent acceleration scheme.  A
tutorial style introduction to this package is available in a vignette on
the CRAN download page or, when the package is loaded in an R session,
with vignette("SQUAREM").

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
%doc %{rlibdir}/SQUAREM/doc
%doc %{rlibdir}/SQUAREM/html
%doc %{rlibdir}/SQUAREM/DESCRIPTION
%doc %{rlibdir}/SQUAREM/NEWS
%{rlibdir}/SQUAREM/INDEX
%{rlibdir}/SQUAREM/LICENSE
RPM build errors:
%{rlibdir}/SQUAREM/help
%{rlibdir}/SQUAREM/Meta
%{rlibdir}/SQUAREM/demo
%{rlibdir}/SQUAREM/R
%{rlibdir}/SQUAREM/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2010.12.1-1
- initial package for Fedora