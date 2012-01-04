%global packname  nFDR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          Nonparametric Estimate of FDR Based on Bernstein Polynomials

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
nFDR is package that implements the nonparametric estimate of FDR based on
Bernstein polynomials. It calculates the proportion of true null
hypotheses, FDR, FNR, and q-values.

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
%doc %{rlibdir}/nFDR/DESCRIPTION
%doc %{rlibdir}/nFDR/html
%{rlibdir}/nFDR/libs
%{rlibdir}/nFDR/Meta
%{rlibdir}/nFDR/R
%{rlibdir}/nFDR/NAMESPACE
%{rlibdir}/nFDR/help
%{rlibdir}/nFDR/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.1-1
- initial package for Fedora