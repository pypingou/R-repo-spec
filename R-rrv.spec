%global packname  rrv
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.4.1
Release:          1%{?dist}
Summary:          Random Return Variables

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-s3x R-mecdf 

BuildRequires:    R-devel tex(latex) R-s3x R-mecdf 

%description
This package is partly based on Markowitz (1952), however considers
empirical distributions. There's a strong emphasis on modelling
conditional portfolio returns as functions of weight. Various "conditional
parameters" are considered, including expected returns and quantile

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
%doc %{rlibdir}/rrv/doc
%doc %{rlibdir}/rrv/html
%doc %{rlibdir}/rrv/DESCRIPTION
%{rlibdir}/rrv/R
%{rlibdir}/rrv/help
%{rlibdir}/rrv/INDEX
%{rlibdir}/rrv/data
%{rlibdir}/rrv/NAMESPACE
RPM build errors:
%{rlibdir}/rrv/Meta

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.1-1
- initial package for Fedora