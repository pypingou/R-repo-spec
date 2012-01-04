%global packname  edd
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.32.0
Release:          1%{?dist}
Summary:          expression density diagnostics

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-golubEsets R-Biobase R-class R-nnet R-xtable 


BuildRequires:    R-devel tex(latex) R-methods R-golubEsets R-Biobase R-class R-nnet R-xtable



%description
tools for evaluating cohort distributions of gene expression levels

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
%doc %{rlibdir}/edd/DESCRIPTION
%doc %{rlibdir}/edd/html
%doc %{rlibdir}/edd/doc
%doc %{rlibdir}/edd/COPYING
%{rlibdir}/edd/INDEX
%{rlibdir}/edd/help
%{rlibdir}/edd/Meta
%{rlibdir}/edd/R
%{rlibdir}/edd/NAMESPACE

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.32.0-1
- initial package for Fedora