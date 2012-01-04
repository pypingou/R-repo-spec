%global packname  simone
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Statistical Inference for MOdular NEtworks (SIMoNe)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mixer 

BuildRequires:    R-devel tex(latex) R-mixer 

%description
The R package simone implements the inference of co-expression networks
based on partial correlation coefficients from either steady-state or
time-course transcriptomic data. Note that with both type of data this
package can deal with samples collected in different experimental
conditions and therefore not identically distributed. In this particular
case, multiple but related networks are inferred on one simone run.

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
%doc %{rlibdir}/simone/html
%doc %{rlibdir}/simone/NEWS
%doc %{rlibdir}/simone/CITATION
%doc %{rlibdir}/simone/DESCRIPTION
%{rlibdir}/simone/help
%{rlibdir}/simone/INDEX
%{rlibdir}/simone/NAMESPACE
%{rlibdir}/simone/Meta
%{rlibdir}/simone/libs
%{rlibdir}/simone/data
%{rlibdir}/simone/demo
%{rlibdir}/simone/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora