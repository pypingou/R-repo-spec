%global packname  cqn
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Conditional quantile normalization

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mclust R-nor1mix R-stats R-preprocessCore R-splines R-quantreg 
Requires:         R-splines 

BuildRequires:    R-devel tex(latex) R-mclust R-nor1mix R-stats R-preprocessCore R-splines R-quantreg
BuildRequires:    R-splines 


%description
A normalization tool for RNA-Seq data, implementing the conditional
quantile normalization method.

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
%doc %{rlibdir}/cqn/doc
%doc %{rlibdir}/cqn/html
%doc %{rlibdir}/cqn/CITATION
%doc %{rlibdir}/cqn/DESCRIPTION
%{rlibdir}/cqn/data
%{rlibdir}/cqn/script
%{rlibdir}/cqn/NAMESPACE
%{rlibdir}/cqn/INDEX
%{rlibdir}/cqn/Meta
%{rlibdir}/cqn/NEWS.Rd
%{rlibdir}/cqn/help
%{rlibdir}/cqn/R

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora