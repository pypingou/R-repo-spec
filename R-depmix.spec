%global packname  depmix
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.10
Release:          1%{?dist}
Summary:          Dependent Mixture Models

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
Fit (multigroup) mixtures of latent Markov models on mixed categorical and
continuous (timeseries) data

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
%doc %{rlibdir}/depmix/CITATION
%doc %{rlibdir}/depmix/DESCRIPTION
%doc %{rlibdir}/depmix/doc
%doc %{rlibdir}/depmix/html
%{rlibdir}/depmix/libs
%{rlibdir}/depmix/data
%{rlibdir}/depmix/Meta
%{rlibdir}/depmix/help
%{rlibdir}/depmix/R
%{rlibdir}/depmix/INDEX
%{rlibdir}/depmix/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.10-1
- initial package for Fedora