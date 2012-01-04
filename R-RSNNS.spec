%global packname  RSNNS
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.4.2
Release:          1%{?dist}
Summary:          Neural Networks in R using the Stuttgart Neural Network Simulator (SNNS)

Group:            Applications/Engineering 
License:          LGPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.4-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-Rcpp 


BuildRequires:    R-devel tex(latex) R-methods R-Rcpp



%description
The Stuttgart Neural Network Simulator (SNNS) is a library containing many
standard implementations of neural networks. This package wraps the SNNS
functionality to make it available from within R. Using the RSNNS
low-level interface, all of the algorithmic functionality and flexibility
of SNNS can be accessed.  Furthermore, the package contains a convenient
high-level interface, so that the most common neural network topologies
and learning algorithms integrate seamlessly into R.

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
%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.2-1
- initial package for Fedora