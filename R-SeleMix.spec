%global packname  SeleMix
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.8.1
Release:          1%{?dist}
Summary:          Selective Editing via Mixture models

Group:            Applications/Engineering 
License:          EUPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-mvtnorm 

%description
Detection of outliers and influential errors using a latent variable

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
%doc %{rlibdir}/SeleMix/doc
%doc %{rlibdir}/SeleMix/html
%doc %{rlibdir}/SeleMix/DESCRIPTION
%{rlibdir}/SeleMix/INDEX
%{rlibdir}/SeleMix/data
%{rlibdir}/SeleMix/Meta
%{rlibdir}/SeleMix/R
%{rlibdir}/SeleMix/NAMESPACE
%{rlibdir}/SeleMix/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.1-1
- initial package for Fedora